import sqlite3
from data_ import Data
from schedule import Schedule
from display import DisplayControl
from population import Population
from geneticalgorithm import GeneticAlgorithm
from flask import Flask, render_template, redirect, url_for, request, g
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired
from prettytable import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "192b9bdd22ab9ed4d12e236c78afcb9a"
Bootstrap(app)

data = Data()
display_control = DisplayControl(data)


# Genetic Algorithm Configuration Form
class ConfigForm(FlaskForm):
    population_size = IntegerField('Population Size', validators=[DataRequired()])
    elitism_number = IntegerField('Elitism Number', validators=[DataRequired()])
    mutation_rate = DecimalField('Mutation Rate', validators=[DataRequired()])
    crossover_rate = DecimalField('Cross Over Rate', validators=[DataRequired()])
    tournament_size = IntegerField('Tournament Size', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/config', methods=['GET', 'POST'])
def config():
    config_form = ConfigForm()

    if config_form.validate_on_submit():
        population_size = config_form.population_size.data
        elitism_number = config_form.elitism_number.data
        mutation_rate = config_form.mutation_rate.data
        crossover_rate = config_form.crossover_rate.data
        tournament_size = config_form.tournament_size.data

        generation_number = 0
        population = Population(population_size, data)
        population.initialize()
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

        ga = GeneticAlgorithm(data, elitism_number, mutation_rate, crossover_rate, tournament_size, population_size)

        while population.get_schedules()[0].get_fitness() != 1.0:
            generation_number += 1
            population = ga.develop_next_gen(population)
            population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

        pop_dict = {}
        fittest_schedule = {}
        for i in range(0, len(population.get_schedules())):
            new_dict = {
                'number': i+1,
                'classes': [str(class_) for class_ in population.get_schedules()[i].get_classes()],
                'NOC': population.get_schedules()[i].get_number_of_conflict(),
                'fitness': population.get_schedules()[i].get_fitness(),
            }
            pop_dict[f'schedule_number {i}'] = new_dict

        for j in range(0, len(population.get_schedules()[0].get_classes())):
            new_dict = {
                'number': j+1,
                'course': population.get_schedules()[0].get_classes()[j].course.name,
                'room': population.get_schedules()[0].get_classes()[j].room.id,
                'instructor': population.get_schedules()[0].get_classes()[j].instructor.name,
                'session': population.get_schedules()[0].get_classes()[j].time_.id + "-->"
                           + population.get_schedules()[0].get_classes()[j].time_.session,
            }
            fittest_schedule[f'class_number {j}'] = new_dict

        # ga = GeneticAlgorithm(data, elitism_number, mutation_rate, crossover_rate, tournament_size, population_size)
        #
        # while population.get_schedules()[0].get_fitness() != 1.0:
        #     generation_number += 1
        #     print(f"Generation > {generation_number}")
        #     population = ga.develop_next_gen(population)
        #     population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        #     display_control.print_population(population)
        #     display_control.print_schedule(population.get_schedules()[0])
        # print("\n\n")
        return render_template("result.html", populations=pop_dict, schedule=fittest_schedule)
    return render_template("config.html", form=config_form)


@app.route('/')
def index():
    all_data = data.all_data
    return render_template("index.html", all_data=all_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
