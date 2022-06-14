const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    follow: userPk => HOST + ACCOUNTS + `${userPk}/` + 'follow/',
    myMovie: username => HOST + ACCOUNTS + 'mymovie/' + `${username}`
  },
  articles: {
    // /커뮤니티 구분 없이 전체 아티클 조회/
    articles: () => HOST + ARTICLES,
    // 각 커뮤니티별 아티클 조회
    community: communityPk => HOST + ARTICLES + `${communityPk}/`,
    article: articlePk => HOST + ARTICLES + `${articlePk}/` + 'detail/',
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    home: () => HOST + MOVIES + 'home/',
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    //create movie comment
    movieComments: moviePk => HOST + MOVIES + `${moviePk}/` + COMMENTS,
    //update, delete
    movieComment: (moviePk, movieCommentPk) =>
      HOST + MOVIES + `${moviePk}/` + COMMENTS + `${movieCommentPk}`,
    movieSearch: searchName => HOST + MOVIES + 'search/' + `${searchName}`,
    movieRecommend: () => HOST + MOVIES + 'recommend/'
  }
}
