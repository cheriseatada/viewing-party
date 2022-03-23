import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()
def test_calculates_watched_average_rating():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.58333)
    assert janes_data == clean_wave_2_data()

# @pytest.mark.skip()
def test_empty_watched_average_rating_is_zero():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)

#@pytest.mark.skip()
def test_most_watched_genre():
    """
    USER_DATA_2 = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],    
}

    FANTASY_1 = {
        "title": "The Lord of the Functions: The Fellowship of the Function",
        "genre": "Fantasy",
        "rating": 4.8
    }
    """

    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == clean_wave_2_data()

# @pytest.mark.skip()
def test_genre_is_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == None
