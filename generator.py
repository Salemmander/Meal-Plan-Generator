import openai
import os
import sys
import config

openai.api_key = config.api_key


def get_calories(sex, weight, height, age):
    match sex:
        case "male":
            return int((10 * weight) + (6.25 * height) - (5 * age) + 5)
        case "female":
            return int((10 * weight) + (6.25 * height) - (5 * age) - 161)


def generate(sex, weight, height, age, avoid):
    cal = get_calories(sex, weight, height, age)

    prompt = "Make 7 day meal plan with a daily caloric intake of {cal} calories\n\
    Format:\n\
    Day\n\
    Breakfast\n\
    Recipe (calories)\n\
    Ingredients\n\
    Cooking instructions\n\
    1.\n\
    2.\n\
    3.\n\
    ...\n\n\n\n\
    Lunch\n\
    Recipe (calories)\n\
    Ingredients\n\
    Cooking instructions\n\
    1.\n\
    2.\n\
    3.\n\
    ...\n\n\n\n\
    Dinner\n\
    Recipe (calories)\n\
    Ingredients\n\
    Cooking instructions\n\
    1.\n\
    2.\n\
    3.\n\
    ...\n\n\n\n\
    Avoid: {avoid}"

    response = openai.Completion.create(
        engine="text-davinci-002", prompt=prompt, temperature=0, max_tokens=2048
    )

    return response["choices"][0]["text"]
