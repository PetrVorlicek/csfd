from src.parser import parse_elements, parse_movie_details


def test_parse_html(sample_movie_ledger_text):
    elem_to_match = "div.article-poster-60 figure a"
    expected_output = [
        "/movie/1",
        "/movie/2",
        "/movie/3",
        "/movie/4",
        "/movie/5",
        "/movie/6",
    ]

    result = parse_elements(sample_movie_ledger_text, elem_to_match)

    assert isinstance(result, list)
    assert result == expected_output


def test_parse_movie_details(sample_movie_page_text):
    expected_title = "Sample Movie Title"
    expected_actors = ["Actor One", "Actor Two", "Actor Three"]

    title, actors = parse_movie_details(sample_movie_page_text)

    assert isinstance(title, str)
    assert title == expected_title
    assert isinstance(actors, list)
    assert actors == expected_actors
