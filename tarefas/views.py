from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
    {
        'nome': 'Agustín Rossi',
        'idade': 30,
        'posicao': 'Goleiro',
        'nascimento': '21/08/1995',
        'cidade': 'Buenos Aires - Argentina',
        'foto': 'img/rossi.webp' },
    {
        'nome': 'Cleiton',
        'idade': 22,
        'posicao': 'Zagueiro',
        'nascimento': '25/04/2003',
        'cidade': 'Taperoá - BA',
        'foto': 'img/cleiton.webp'},
    {
        'nome': 'Léo Ortiz',
        'idade': 29,
        'posicao': 'Zagueiro',
        'nascimento': '03/01/1996',
        'cidade': 'Porto Alegre - RS',
        'foto': 'img/leo.webp'},
    {
        'nome': 'Guillermo Varela',
        'idade': 32,
        'posicao': 'Lateral Direito',
        'nascimento': '24/09/1993',
        'cidade': 'Montevidéu - Uruguai',
        'foto': 'img/varela.webp'},
    {
        'nome': 'Matias Viña',
        'idade': 27,
        'posicao': 'Lateral Esquerdo',
        'nascimento': '09/11/1997',
        'cidade': 'Empalme Olmos - Uruguai',
        'foto': 'img/matias.webp'},
    {
        'nome': 'Erick Pulgar',
        'idade': 31,
        'posicao': 'Volante',
        'nascimento': '15/01/1994',
        'cidade': 'Antofagasta - Chile',
        'foto': 'img/erick.webp'},
    {
        'nome': 'Allan Rodrigues',
        'idade': 28,
        'posicao': 'Volante',
        'nascimento': '03/03/1997',
        'cidade': 'São Paulo - SP',
        'foto': 'img/allan.webp'},
    {
        'nome': 'Diego Nicolas',
        'idade': 28,
        'posicao': 'Meio Campista',
        'nascimento': '01/06/1997',
        'cidade': 'Montevidéu - Uruguai',
        'foto': 'img/de la cruz.webp'},
    {
        'nome': 'Jorge Carrascal',
        'idade': 27,
        'posicao': 'Meio Campista',
        'nascimento': '25/05/1998',
        'cidade': 'Cartagena',
        'foto': 'img/carrascal.webp'},
    {
        'nome': 'Pedro',
        'idade': 28,
        'posicao': 'Atacante',
        'nascimento': '20/06/1997',
        'cidade': 'Rio de Janeiro - RJ',
        'foto': 'img/pedro.webp'},
    {
        'nome': 'Bruno Henrique',
        'idade': 34,
        'posicao': 'Atacante',
        'nascimento': '30/12/1990',
        'cidade': 'Belo Horizonte - MG',
        'foto': 'img/bruno.webp'},
    ]
    context = {
        "jogadores": jogadores,
    }
    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")