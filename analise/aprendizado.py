from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

from nltk.corpus import stopwords

from material.separador import DATA_SET
from material.separador import LISTA_TESTE
from material.separador import separador


class Learn():
    """
    Classe responsavel pelo aprendizado da maquina e classificação.
    """
    def __init__(self):
        # treina e classifica
        self.classificator = SVC(kernel='linear')
        self.training_set, self.labels = separador(DATA_SET)
        self.text, self.label_correct = separador(LISTA_TESTE)

    def start(self):
        """
        Método que inicia aprendizado.
        """
        # elimina stopwords, analisa palavra por palavra, deixa em caixa baixa
        # remove acentos e usa idf.
        self.tf_vectorizer = TfidfVectorizer(
                                        stop_words=stopwords.words('english'),
                                        analyzer='word',
                                        ngram_range=(1, 2),
                                        lowercase=True,
                                        use_idf=True,
                                        strip_accents='unicode'
                                        )

        # atribui peso a cada palavra
        feature = self.tf_vectorizer.fit_transform(self.training_set)
        # classifica usando as features(treino)
        self.classificator.fit(feature, self.labels)

    def one_zero(self):
        """
        Método que efetua teste de acurácia.
        """
        text, label_correct = separador(LISTA_TESTE)
        # vetoriza utilizando apenas frses sem labels
        vector_text = self.tf_vectorizer.transform(text)
        # efetua predição, adicionando labels
        predictions = self.classificator.predict(vector_text)
        erro = 0
        acerto = 0
        # laço que compara predição com label corretos e faz contagem
        for prediction, label_correct in zip(predictions, label_correct):
            if label_correct == prediction:
                acerto+= 1
            else:
                erro+= 1

        erro_acerto = f'{erro} erros e {acerto} acertos/300 frases.'
        acuracia = f'{acerto/3}% de acurácia!'
        # retorna numero de erros, acerto e acurácia
        return erro_acerto, acuracia

    def one(self, data):
        """
        Método que classifica frase especifica.
        """
        text = [data]
        # vetoriza utilizando apenas frse sem label
        vector_text = self.tf_vectorizer.transform(text)
        # efetua predição, adicionando label
        prediction = self.classificator.predict(vector_text)
        if '1' in prediction:
            return 'FRASE POSITIVA!!!'
        if '0' in prediction:
            return 'FRASE NEGATIVA!!!'
