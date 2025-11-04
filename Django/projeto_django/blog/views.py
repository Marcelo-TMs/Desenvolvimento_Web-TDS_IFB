from django.shortcuts import render

PROJETOS = [
    {
        'titulo': 'Projeto 1',
        'descricao': 'Descrição breve do Projeto 1',
        'link': '#',
        'imagem': 'img/Android.png',
    },
    {
        'titulo': 'Projeto 2',
        'descricao': 'Descrição breve do Projeto 2',
        'link': '#',
        'imagem': 'img/Android.png',
    },
    {
        'titulo': 'Projeto 3',
        'descricao': 'Descrição breve do Projeto 3',
        'link': '#',
        'imagem': 'img/Android.png',
    }
]

def index(request):
    title_page = "Página Principal"

    return render(request, 'blog/index.html', {
        'title_page': title_page,
        'projetos': PROJETOS
    })