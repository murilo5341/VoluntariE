from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/voluntario")
templates = obter_jinja_templates("templates/voluntario")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/voluntarioassinante", response_class=HTMLResponse)
async def get_voluntarioassinante(request: Request):
    return templates.TemplateResponse("pages/voluntarioassinante.html", {"request": request})

@router.get("/desativarconta", response_class=HTMLResponse)
async def get_desativarconta(request: Request):
    return templates.TemplateResponse("pages/desativarconta.html", {"request": request})

@router.get("/avaliacoes", response_class=HTMLResponse)
async def get_avaliacoes(request: Request):
    return templates.TemplateResponse("pages/avaliacoes.html", {"request": request})

@router.get("/ingressarprojeto", response_class=HTMLResponse)
async def get_ingressarProjeto(request: Request):
    return templates.TemplateResponse("pages/ingressarProjeto.html", {"request": request})

@router.get("/assinatura", response_class=HTMLResponse)
async def get_assinatura(request: Request):
    return templates.TemplateResponse("pages/assinatura.html", {"request": request})

@router.get("/criarprojeto", response_class=HTMLResponse)
async def get_criarProjeto(request: Request):
    return templates.TemplateResponse("pages/criarProjeto.html", {"request": request})

@router.get("/doacao", response_class=HTMLResponse)
async def get_doacao(request: Request):
    return templates.TemplateResponse("pages/doacao.html", {"request": request})

@router.get("/excluirprojeto", response_class=HTMLResponse)
async def get_excluirProjeto(request: Request):
    return templates.TemplateResponse("pages/excluirProjeto.html", {"request": request})

@router.get("/projetosingressados", response_class=HTMLResponse)
async def get_projetosIngressados(request: Request):
    return templates.TemplateResponse("pages/projetosingressados.html", {"request": request})

@router.get("/membrosprojeto", response_class=HTMLResponse)
async def get_membrosProjeto(request: Request):
    return templates.TemplateResponse("pages/membrosProjeto.html", {"request": request})

@router.get("/solicitarmoderacao", response_class=HTMLResponse)
async def get_solicitarmoderacao(request: Request):
    return templates.TemplateResponse("pages/solicitacaoModeracao.html", {"request": request})

@router.get("/notificacaovoluntario", response_class=HTMLResponse)
async def get_notificacaovoluntario(request: Request):
    return templates.TemplateResponse("pages/notificacaoVoluntario.html", {"request": request})

@router.get("/alterarsenha", response_class=HTMLResponse)
async def get_alterarsenha(request: Request):
    return templates.TemplateResponse("pages/alterarsenha.html", {"request": request})