from bs4 import BeautifulSoup


def parse_elements(page_text: str, elem_to_match: str) -> list[str]:
    """
    Parse element text from the given HTML for further processing.
    """
    soup = BeautifulSoup(page_text, "html.parser")
    anchors = []
    for item in soup.select(elem_to_match):
        anchors.append(item["href"])
    return anchors


def _parse_movie_title(soup: BeautifulSoup) -> str:
    title = soup.find("h1")
    if not title:
        raise ValueError("No movie title found in the page text.")
    return title.get_text(strip=True)


def _parse_actors(soup: BeautifulSoup) -> list[str] | None:
    creators_tag = soup.find(id="creators")
    if not creators_tag:
        raise ValueError("No creators found in the page text.")

    divs = creators_tag.find_all("div", recursive=False)

    for div in divs:
        h4 = div.find("h4")
        if h4 and h4.get_text(strip=True) == "Hrají:":
            anchor_texts = [a.get_text(strip=True) for a in div.find_all("a")]
            # "více" is not an actor name, so we filter it out
            if anchor_texts:
                anchor_texts = [text for text in anchor_texts if text != "více"]
            return anchor_texts


def parse_movie_details(page_text: str) -> tuple[str, list[str] | None]:
    """
    Parse movie title and actors from the given HTML for further processing.
    """
    soup = BeautifulSoup(page_text, "html.parser")

    title = _parse_movie_title(soup)
    actors = _parse_actors(soup)

    return title, actors
