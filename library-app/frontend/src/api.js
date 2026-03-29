import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE,
});

// Books
export const getBooks = () => api.get('/books');
export const getBook = (id) => api.get(`/books/${id}`);
export const createBook = (book) => api.post('/books', book);
export const updateBook = (id, book) => api.patch(`/books/${id}`, book);
export const deleteBook = (id) => api.delete(`/books/${id}`);

// Ownership
export const addOwnership = (bookId, ownership) => api.post(`/books/${bookId}/ownership`, ownership);
export const getOwnership = (bookId) => api.get(`/books/${bookId}/ownership`);

// Reading Progress
export const addProgress = (bookId, progress) => api.post(`/books/${bookId}/progress`, progress);
export const getProgress = (bookId) => api.get(`/books/${bookId}/progress`);
export const updateProgress = (progressId, progress) => api.patch(`/progress/${progressId}`, progress);
export const deleteProgress = (progressId) => api.delete(`/progress/${progressId}`);
