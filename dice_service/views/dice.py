import os

from flakon import SwaggerBlueprint
from flask import jsonify, abort, request

from dice_service.database import DiceSet, Die

YML = os.path.join(os.path.dirname(__file__), '..', 'static', 'dice-api.yaml')
dice = SwaggerBlueprint('dice', '__name__', swagger_spec=YML)


@dice.operation('getSets')
def _sets():
    all_sets = DiceSet.query.all()
    # return 200 if there is more than 1 set (2xx Success OK)
    # return 204 if there is no set (2xx Success No Content)
    code = 200 if len(all_sets) > 0 else 204
    return jsonify([s.to_json() for s in all_sets]), code


@dice.operation('getSet')
def _set(id_set):
    asked_set = DiceSet.query.filter_by(id=id_set).first()

    if asked_set is None:
        abort(404, 'DiceSet not found')
    else:
        return jsonify(asked_set.to_json())


@dice.operation('rollSet')
def _roll_set(id_set):
    asked_set = DiceSet.query.filter_by(id=id_set).first()
    dice_number = request.args.get('dice_number')

    if asked_set is None:
        abort(404, 'DiceSet not found')
    elif dice_number is None:
        abort(404, "Specify number of dice you want to roll")
    elif dice_number not in range(2, 7):
        abort(400, "Number of dice to roll must be between 2 and 6")
    else:
        return jsonify(asked_set.roll_set(dice_number))
