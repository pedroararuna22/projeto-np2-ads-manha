
# tree_logic.py — você edita APENAS este arquivo nesta atividade.

class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):

    while not is_leaf(node):
        if not answers:
            raise ValueError("Faltam respostas para concluir a decisão.")

        resposta = answers.pop(0).lower().strip()

        if resposta == "nao":
            resposta = "não"

        if resposta == "sim":
            node = node.yes
        elif resposta == "não":
            node = node.no
        else:
            raise ValueError(f"Resposta inválida: {resposta}")

    return node.question    

