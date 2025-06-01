import pytest


@pytest.fixture
def sample_movie_ledger_text():
    return """
    <html>
        <body>
            <div id="article1" class="article-poster-60">
                <figure>
                    <a href="/movie/1">Movie 1</a>
                </figure>
                <figure>
                    <a href="/movie/2">Movie 2</a>
                </figure>
            </div>
            <div id="article2" class="article-poster-60">
                <figure>
                    <a href="/movie/3">Movie 3</a>
                </figure>
                <figure>
                    <a href="/movie/4">Movie 4</a>
                </figure>
            </div>
            <div id="article3" class="article-poster-60">
                <figure>
                    <a href="/movie/5">Movie 5</a>
                </figure>
                <figure>
                    <a href="/movie/6">Movie 6</a>
                </figure>
            </div>
        </body>
    </html>
    """


@pytest.fixture
def sample_movie_page_text():
    return """
    <html>
        <body>
            <h1>Sample Movie Title</h1>
            <div id="creators">
                <div>
                    <h4>Hrají:</h4>
                    <a href="/actor/1">Actor One</a>
                    <a href="/actor/2">Actor Two</a>
                    <a href="/actor/3">Actor Three</a>
                    <a href="/more">více</a>
                </div>
            </div>
        </body>
    </html>
    """
