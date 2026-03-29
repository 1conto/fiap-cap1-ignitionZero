import random
from dataclasses import dataclass

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix


modulos_criticos = [
    "flight_computer",
    "navigation_system",
    "attitude_control",
    "communication_system",
    "power_system",
    "propulsion_system",
]


class ModulosCriticos:
    def __init__(self, nome):
        self.nome = nome
        self.status = None

    def testar_status(self):
        # 95% de chance de estar OK e 5% de chance de falha
        self.status = random.choices([True, False], weights=[0.95, 0.05])[0]
        return self.status


class Telemetria:
    def __init__(self, list_modulos):
        self.temperatura_interna = None
        self.temperatura_externa = None
        self.integridade_estrutural = None
        self.voltagem_bateria = None
        self.corrente_bateria = None
        self.nivel_bateria = None
        self.capacidade_bateria = None
        self.energia_disponivel = None
        self.carga_potencia = None
        self.perda_energia = None
        self.pressao_tanque = None
        self.modulos = [ModulosCriticos(modulo) for modulo in list_modulos]
        self.dict_validacoes = None
        self.dict_auditoria = None
        self.dict_valores = None
        self.decisao_decolagem = None

    @property
    def valores(self):
        return self.dict_valores

    def testar_todos_modulos(self):
        for modulo in self.modulos:
            modulo.testar_status()
        return self.modulos

    def captura_temperatura_interna(self):
        self.temperatura_interna = max(18, min(40, int(random.gauss(24, 6))))
        return self.temperatura_interna

    def captura_temperatura_externa(self):
        self.temperatura_externa = max(-10, min(35, int(random.gauss(25, 8))))
        return self.temperatura_externa

    def captura_voltagem_bateria(self):
        self.voltagem_bateria = random.uniform(46, 52)
        return self.voltagem_bateria

    def captura_corrente_bateria(self):
        self.corrente_bateria = random.uniform(20, 120)
        return self.corrente_bateria

    def captura_energy_lvl(self):
        self.nivel_bateria = random.betavariate(10, 1)
        return self.nivel_bateria

    def captura_capacidade_bateria(self):
        self.capacidade_bateria = random.uniform(80, 120)
        return self.capacidade_bateria

    def captura_energia_disponivel(self):
        self.energia_disponivel = (
            self.voltagem_bateria * self.capacidade_bateria * self.nivel_bateria
        ) / 1000
        return self.energia_disponivel

    def captura_carga_potencia(self):
        self.carga_potencia = random.uniform(5, 25)
        return self.carga_potencia

    def captura_perda_energia(self):
        self.perda_energia = random.uniform(2, 8)
        return self.perda_energia

    def captura_pressao_tanque(self):
        self.pressao_tanque = random.gauss(70, 5)
        return self.pressao_tanque

    def captura_integridade_estrutural(self):
        self.integridade_estrutural = random.choices([True, False], weights=[0.9, 0.1])[0]
        return self.integridade_estrutural

    def captura_infos_telemetria(self):
        self.captura_temperatura_interna()
        self.captura_temperatura_externa()
        self.captura_integridade_estrutural()
        self.captura_energy_lvl()
        self.captura_pressao_tanque()

    def captura_infos_energia(self):
        self.captura_voltagem_bateria()
        self.captura_corrente_bateria()
        self.captura_capacidade_bateria()
        self.captura_carga_potencia()
        self.captura_energia_disponivel()
        self.captura_perda_energia()

    def define_valores_info_energia(self):
        self.captura_infos_energia()
        modulos_energia = [
            "voltagem_bateria",
            "corrente_bateria",
            "capacidade_bateria",
            "carga_potencia",
            "energia_disponivel",
            "perda_energia",
        ]
        for modulo in modulos_energia:
            self.dict_valores[modulo] = getattr(self, modulo)

    def validacoes_telemetria(self, valores_seguros):
        self.testar_todos_modulos()
        self.captura_infos_telemetria()
        dict_validacoes = {}
        dict_auditoria = {}
        dict_valores = {}

        for sensor, valor_seguro in valores_seguros.items():
            valor = getattr(self, sensor)
            dict_valores[sensor] = valor

            if sensor == "modulos":
                status_modulos = [modulo.status for modulo in valor]
                modulos_falhos = [modulo.nome for modulo in valor if not modulo.status]
                dict_validacoes[sensor] = all(status_modulos)
                dict_valores[sensor] = {modulo.nome: modulo.status for modulo in valor}
                dict_auditoria[sensor] = {
                    "valor_atual": all(status_modulos),
                    "regra": (
                        f"Os módulos {', '.join(modulos_falhos)}"
                        f"{' não ' if modulos_falhos else ' '}estão seguros."
                    ),
                }

            elif isinstance(valor_seguro, dict):
                minimo = valor_seguro["min"]
                maximo = valor_seguro["max"]
                dict_validacoes[sensor] = minimo <= valor <= maximo
                dict_auditoria[sensor] = {
                    "valor_atual": valor,
                    "regra": f"{sensor} deve estar entre {minimo} e {maximo}.",
                }

            elif isinstance(valor_seguro, bool):
                dict_validacoes[sensor] = valor == valor_seguro
                dict_auditoria[sensor] = {
                    "valor_atual": valor,
                    "regra": f"{sensor} deve ser {valor_seguro}.",
                }

        self.dict_validacoes = dict_validacoes
        self.dict_auditoria = dict_auditoria
        self.dict_valores = dict_valores
        self.define_valores_info_energia()

    def valida_decolagem(self):
        self.decisao_decolagem = (
            "PRONTO PARA DECOLAR"
            if all(self.dict_validacoes.values())
            else "DECOLAGEM ABORTADA"
        )
        self.dict_valores["Decolagem"] = self.decisao_decolagem
        self.dict_valores["Motivo"] = self.dict_auditoria
        self.dict_valores["Validações"] = self.dict_validacoes
        return self.decisao_decolagem


valores_seguros = {
    "temperatura_interna": {"min": 18, "max": 30},
    "temperatura_externa": {"min": 15, "max": 35},
    "nivel_bateria": {"min": 0.8, "max": 1},
    "pressao_tanque": {"min": 60, "max": 80},
    "integridade_estrutural": True,
    "modulos": True,
}


@dataclass
class ResultadoAnomalia:
    precisao_anomalia: float
    recall_anomalia: float
    total_anomalias_injetadas: int
    total_anomalias_detectadas: int


def gerar_dataset_telemetria(numero_ocorrencias=1000, seed=42):
    random.seed(seed)
    telemetria_geracao = Telemetria(modulos_criticos)
    registros = []

    for _ in range(numero_ocorrencias):
        telemetria_geracao.validacoes_telemetria(valores_seguros)
        telemetria_geracao.valida_decolagem()
        registros.append(telemetria_geracao.valores.copy())

    df = pd.DataFrame(registros)
    df_modulos_expandido = df["modulos"].apply(pd.Series)
    df = pd.concat([df.drop("modulos", axis=1), df_modulos_expandido], axis=1)

    for coluna in df.columns:
        if df[coluna].dtype == bool:
            df[coluna] = df[coluna].astype(int)

    colunas_modelo = [
        "temperatura_interna",
        "temperatura_externa",
        "nivel_bateria",
        "pressao_tanque",
        "integridade_estrutural",
        "flight_computer",
        "navigation_system",
        "attitude_control",
        "communication_system",
        "power_system",
        "propulsion_system",
    ]
    return df[colunas_modelo].copy()


def inserir_anomalias_manuais(df, seed=42, fracao_anomalia=0.05):
    df_anomalias = df.copy()
    total_anomalias = max(1, int(len(df_anomalias) * fracao_anomalia))
    indices_anomalia = df_anomalias.sample(total_anomalias, random_state=seed).index

    # Injeção manual de valores extremos e combinações improváveis
    df_anomalias.loc[indices_anomalia, "temperatura_interna"] = 55
    df_anomalias.loc[indices_anomalia, "temperatura_externa"] = -35
    df_anomalias.loc[indices_anomalia, "nivel_bateria"] = 0.05
    df_anomalias.loc[indices_anomalia, "pressao_tanque"] = 120
    df_anomalias.loc[indices_anomalia, "integridade_estrutural"] = 0

    rotulo_real = pd.Series(0, index=df_anomalias.index)
    rotulo_real.loc[indices_anomalia] = 1
    return df_anomalias, rotulo_real


def treinar_e_validar_isolation_forest(df_treino, df_teste, y_real_anomalia, seed=42):
    if_model = IsolationForest(
        n_estimators=300,
        contamination=float(y_real_anomalia.mean()),
        random_state=seed,
    )
    if_model.fit(df_treino)

    predicao_bruta = if_model.predict(df_teste)
    y_pred_anomalia = pd.Series((predicao_bruta == -1).astype(int), index=df_teste.index)

    print("=== Isolation Forest - Reconhecimento de Anomalias ===")
    print(classification_report(y_real_anomalia, y_pred_anomalia, digits=4))
    print("Matriz de confusão [normal, anomalia]:")
    print(confusion_matrix(y_real_anomalia, y_pred_anomalia))

    anomalias_detectadas = int((y_pred_anomalia & y_real_anomalia).sum())
    return ResultadoAnomalia(
        precisao_anomalia=float(
            classification_report(y_real_anomalia, y_pred_anomalia, output_dict=True)["1"]["precision"]
        ),
        recall_anomalia=float(
            classification_report(y_real_anomalia, y_pred_anomalia, output_dict=True)["1"]["recall"]
        ),
        total_anomalias_injetadas=int(y_real_anomalia.sum()),
        total_anomalias_detectadas=anomalias_detectadas,
    )


def exemplo_reconhecimento_anomalias():
    print("Gerando dataset base de telemetria...")
    df_normal = gerar_dataset_telemetria(numero_ocorrencias=1200, seed=42)

    # Treinamos no comportamento normal
    df_treino = df_normal.sample(frac=0.7, random_state=42)
    df_teste_base = df_normal.drop(df_treino.index)

    print("Injetando anomalias manuais no conjunto de teste...")
    df_teste_anomalo, y_anomalia_real = inserir_anomalias_manuais(
        df_teste_base, seed=42, fracao_anomalia=0.08
    )

    resultado = treinar_e_validar_isolation_forest(
        df_treino=df_treino,
        df_teste=df_teste_anomalo,
        y_real_anomalia=y_anomalia_real,
        seed=42,
    )

    print("\nResumo do experimento:")
    print(f"- Anomalias injetadas manualmente: {resultado.total_anomalias_injetadas}")
    print(f"- Anomalias detectadas: {resultado.total_anomalias_detectadas}")
    print(f"- Precisão (classe anomalia): {resultado.precisao_anomalia:.2%}")
    print(f"- Recall (classe anomalia): {resultado.recall_anomalia:.2%}")


if __name__ == "__main__":
    exemplo_reconhecimento_anomalias()
