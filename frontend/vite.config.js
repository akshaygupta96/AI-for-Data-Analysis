export default {
  server: {
    proxy: {
      '/upload': 'http://localhost:8000',
      '/ask': 'http://localhost:8000'
    }
  }
}
