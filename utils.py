import json

from flask import app
from werkzeug.exceptions import abort


def load_candidates() -> list[dict]:
    '''загрузка кандидатов'''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        new_file = json.load(file)
        file.close()
        return new_file


def get_all_candidates() -> list[dict]:
    '''Загрузка всех кандидатов'''
    return load_candidates()


def get_format_candidates(candidates: list[dict]) -> str:
    '''Форматирование списка кандидатов'''

    result = '<pre>'
    for candidate in candidates:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
        """
    result += '</pre>'
    return result

def get_candidate_by_id(uid: int) -> dict:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    app.logger.debug('Candidate does not found')
    abort(404)


def get_candidate_by_skill(skill) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    if len(result) == 0:
        app.logger.debug('Position does not found')
        abort(404)


    return result



