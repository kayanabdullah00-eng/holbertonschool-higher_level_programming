const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.querySelector('#list_movies');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const newItem = document.createElement('li');
      newItem.textContent = movie.title;
      listMovies.appendChild(newItem);
    });
  });

