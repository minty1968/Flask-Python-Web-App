"""Routes for lottery pages."""
from flask import Blueprint, render_template
from flask_login import login_required
import random
from pymongo import MongoClient
from application.models.lottery import Lottery


# Blueprint Configuration
lottery_bp = Blueprint('lottery', __name__,
                       template_folder='application/templates/lottery/',
                       static_folder='application/static')


@lottery_bp.route('/lottery/national-lottery', methods=['GET'])
def lotto():
    """National Lottery route.  First we generate 6 numbers between 1 and 59, then sort them. """

    random_nums = random.sample(range(1, 59), 6)
    sorted_random_nums = sorted(random_nums)

    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.lottery
    collection = db['lotto']
    lottery_data = collection.find({})

    return render_template('lottery/lotto.html',
                           title='Sharpe Digital Solutions | National Lottery',
                           template='lottery-template main', lottery_data=lottery_data,
                           body="National Lottery", sorted_random_nums=sorted_random_nums)


@lottery_bp.route('/lottery/national-lottery-hotpicks', methods=['GET'])
def lottoHP():
    """National Lottery Hotpicks route.  First we generate x numbers between 1 and 59, then sort them. """

    random_nums = random.sample(range(1, 59), 6)
    sorted_random_nums = sorted(random_nums)

    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.lottery
    collection = db['lotto-hotpicks']
    lottery_data = collection.find({})

    return render_template('lottery/lottoHP.html',
                           title='Sharpe Digital Solutions | National Lottery Hotpicks',
                           template='lottery-template main', lottery_data=lottery_data,
                           body="National Lottery Hotpicks", sorted_random_nums=sorted_random_nums)


@lottery_bp.route('/lottery/euromillions', methods=['GET'])
def euro():
    """Euromillions route.  First we generate 5 numbers between 1 and 50, then sort them.
        We then generate two bonus numbers between 1 and 12."""

    random_nums = random.sample(range(1, 50), 5)
    sorted_random_nums = sorted(random_nums)

    bonus_nums = random.sample(range(1, 12), 2)
    sorted_bonus_nums = sorted(bonus_nums)

    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.lottery
    collection = db['euromillions']
    lottery_data = collection.find({})

    return render_template('lottery/euro.html', lottery_data=lottery_data,
                           title='Sharpe Digital Solutions | Euromillions',
                           template='lottery-template main', sorted_bonus_nums=sorted_bonus_nums,
                           body="Euromillions", sorted_random_nums=sorted_random_nums)


@lottery_bp.route('/lottery/euromillions-hotpicks', methods=['GET'])
def euroHP():
    """Euromillions Hotpicks route.  First we generate x numbers between 1 and 50, then sort them. """

    random_nums = random.sample(range(1, 50), 5)
    sorted_random_nums = sorted(random_nums)

    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.lottery
    collection = db['euromillions-hotpicks']
    lottery_data = collection.find({})

    return render_template('lottery/euroHP.html',
                           title='Sharpe Digital Solutions | Euromillions Hotpicks',
                           template='lottery-template main', lottery_data=lottery_data,
                           body="Euromillions Hotpicks", sorted_random_nums=sorted_random_nums)


@lottery_bp.route('/lottery/set-for-life', methods=['GET'])
def s4l():
    """Set for Life route.  First we generate 5 numbers between 1 and 47, then sort them.
        We then generate a bonus number between 1 and 10."""

    random_nums = random.sample(range(1, 47), 5)
    sorted_random_nums = sorted(random_nums)

    bonus_nums = random.sample(range(1, 10), 1)

    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.lottery
    collection = db['set-for-life']
    lottery_data = collection.find({})

    return render_template('lottery/s4l.html', lottery_data=lottery_data,
                           title='Sharpe Digital Solutions | Set for Life',
                           template='lottery-template main', bonus_nums=bonus_nums,
                           body="Set for Life", sorted_random_nums=sorted_random_nums)


@lottery_bp.route('/lottery/thunderball', methods=['GET'])
def thunder():
    """Thunderball route.  First we generate 5 numbers between 1 and 39, then sort them.
        We then generate a bonus number between 1 and 14."""

    random_nums = random.sample(range(1, 39), 5)
    sorted_random_nums = sorted(random_nums)

    bonus_nums = random.sample(range(1, 14), 1)

    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.lottery
    collection = db['thunderball']
    lottery_data = collection.find({})

    return render_template('lottery/thunder.html', lottery_data=lottery_data,
                           title='Sharpe Digital Solutions | Thunderball',
                           template='lottery-template main', bonus_nums=bonus_nums,
                           body="Thunderball", sorted_random_nums=sorted_random_nums)
