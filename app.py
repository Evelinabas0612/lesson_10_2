from flask import Flask

from utils import get_all_candidates, get_format_candidates, get_candidate_by_id, get_candidate_by_skill

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def page_main():
    '''Гланая страница'''
    candidates: list[dict] = get_all_candidates()
    result: str = get_format_candidates(candidates)
    return result

@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    '''Поиск кандидата по id'''
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src = "{candidate["picture"]}">'
    result += get_format_candidates([candidate])
    return result

@app.route('/skills/<skill>')
def page_skills(skill):
    '''Поиск по специализации'''
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = get_format_candidates(candidates)
    return result


app.run()
