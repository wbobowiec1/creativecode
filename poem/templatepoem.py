{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Welcome To Colaboratory",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/wbobowiec1/CreativeCodeClass/blob/master/Copy_of_Welcome_To_Colaboratory.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hwAFpJLspoW4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import random\n",
        "import requests \n",
        "from textblob import TextBlob\n",
        "import nltk\n",
        "nltk.download('punkt')\n",
        "nltk.download('averaged_perceptron_tagger')\n",
        "\n",
        "with open(\"/content/Selected Poems by Robert Frost.txt\") as newText:\n",
        "  poemText = newText.read()\n",
        "\n",
        "wordList = textFile.split(\" \")\n",
        "\n",
        "newBlob = TextBlob(poemText)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AczS3TUMoekl",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "poem_text = \"\"\"\n",
        "Our Yin-Yang Love\n",
        " \n",
        "You are my Yin and I am your Yang.\n",
        "Complete only with one another.\n",
        "Our love is no sunshine and rainbows \n",
        "But it is like no other. \n",
        " \n",
        "Two people and two personalities\n",
        "With differences, though our hearts resides.\n",
        "Each of us owns a bit of the other \n",
        "For we are the same coin, just two sides.\n",
        " \n",
        "Distance separates us but fear not \n",
        "We’ll meet soon, for we are like two rivers\n",
        "Ever flowing til they come together again.\n",
        "Beauty of our resolve gives me shivers.\n",
        " \n",
        "Like life and death, our time will eventually end \n",
        "But til then, honey, say you won’t let go.\n",
        "Let me be your rain in your desert\n",
        "And won’t you be my light to my shadow.\n",
        " \n",
        "There’s so much more I could say but...\n",
        "I’ve realized something.\n",
        "For us, falling in love wasn’t just a moment \n",
        "It’s a forever and always kind of thing \n",
        " \n",
        "\"\"\"\n",
        "\n",
        "poemBlob = TextBlob(poem_text)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3mZ3jIAcx8ra",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "poemBlob.tags"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wQ3jR5C3vpm2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "singular_nouns = []\n",
        "plural_nouns = []\n",
        "adjectives = []\n",
        "\n",
        "for word,pos in newBlob.tags:\n",
        "  if(pos == 'NN'):\n",
        "    singular_nouns.append(word)\n",
        "\n",
        "  if(pos == 'NNS'):\n",
        "    plural_nouns.append(word)\n",
        "    \n",
        "  if(pos == 'JJ'):\n",
        "    adjectives.append(word)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BJUa7wCfvGlQ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 492
        },
        "outputId": "e2b5a8a2-c09a-45d2-d94f-d90da8a8615c"
      },
      "source": [
        "print(\"Our \" + random.choice(adjectives) + \" Love\")\n",
        "print(\"\")\n",
        "print(random.choice(singular_nouns) + \" are my \" + random.choice(adjectives) + \"and \" + random.choice(singular_nouns) + \"am your \" + random.choice(adjectives) + \".\")\n",
        "print(\"Complete only with \" + random.choice(plural_nouns) + \".\")\n",
        "print(\"Our love is no \" + random.choice(singular_nouns) + \"and \" + random.choice(plural_nouns))\n",
        "print(\"But it is like \" + random.choice(adjectives) + \".\")\n",
        "print(\"\")\n",
        "print(\"Two \" + random.choice(plural_nouns) + \"and two \" + random.choice(plural_nouns))\n",
        "print(\"With differences, though our \" + random.choice(plural_nouns) + \" resides.\")\n",
        "print(random.choice(plural_nouns) + \" owns a bit of \" + random.choice(singular_nouns))\n",
        "print(random.choice(plural_nouns) + \"are \" + random.choice(adjectives) + random.choice(adjectives) + \".\")\n",
        "print(\"\")\n",
        "print(\"Distance separates \" + random.choice(plural_nouns) + \" but fear not\")\n",
        "print(random.choice(plural_nouns) + \" will meet soon, for \" + random.choice(plural_nouns) + \" are like \" + random.choice(plural_nouns))\n",
        "print(\"Ever flowing til \" + random.choice(plural_nouns) + \" come together again.\")\n",
        "print(random.choice(adjectives) + \" of our \" + random.choice(singular_nouns) + \" gives me \" + random.choice(plural_nouns) + \".\")\n",
        "print(\"\")\n",
        "print(\"Like \" + random.choice(singular_nouns) + \" and \" + random.choice(singular_nouns) + \", our \" + random.choice(singular_nouns) + \"will eventually end\")\n",
        "print(\"But til then, \" + random.choice(singular_nouns) + \", say \" + random.choice(singular_nouns) + \" won’t let go.\")\n",
        "print(\"Let \" + random.choice(singular_nouns) + \" be it's \" + random.choice(singular_nouns) + \" in it's \" + random.choice(singular_nouns))\n",
        "print(\"And won’t \" + random.choice(singular_nouns) + \" be \" + random.choice(singular_nouns) + \" it's \" + random.choice(singular_nouns) + \" to it's \" + random.choice(singular_nouns) + \".\")\n",
        "print(\"\")\n",
        "print(\"There’s so much \" + random.choice(adjectives) + \" \" + random.choice(singular_nouns) + \" could say but...\")\n",
        "print(random.choice(singular_nouns) + \" have realized something.\")\n",
        "print(\"For \" + random.choice(plural_nouns) + \", falling in love wasn’t just \" + random.choice(adjectives))\n",
        "print(\"It’s a forever and always kind of thing\")\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Our ready Love\n",
            "\n",
            "one are my suspectand moonam your weary.\n",
            "Complete only with characters.\n",
            "Our love is no pairand stones\n",
            "But it is like sure.\n",
            "\n",
            "Two stonesand two papers\n",
            "With differences, though our men resides.\n",
            "sides owns a bit of devil\n",
            "handsare personalsure.\n",
            "\n",
            "Distance separates woods but fear not\n",
            "things will meet soon, for sideways are like miles\n",
            "Ever flowing til arms come together again.\n",
            "likely of our mist gives me cows.\n",
            "\n",
            "Like disc and praise, our riverwill eventually end\n",
            "But til then, field, say load won’t let go.\n",
            "Let year be it's latch in it's —-and\n",
            "And won’t o'clock be coat it's offence to it's talk.\n",
            "\n",
            "There’s so much such glass could say but...\n",
            "democrat-load have realized something.\n",
            "For lines, falling in love wasn’t just good\n",
            "It’s a forever and always kind of thing\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
