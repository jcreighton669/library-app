import React, { useState, useEffect } from 'react';
import { getBooks, createBook, deleteBook } from './api';
import BookList from './components/BookList';
import BookForm from './components/BookForm';
import './App.css';

function App() {
  const [books, setBooks] = useState([]);
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    loadBooks();
  }, []);

  const loadBooks = async () => {
    try {
      const response = await getBooks();
      setBooks(response.data);
    } catch (error) {
      console.error('Error loading books:', error);
    }
  };

  const handleAddBook = async (bookData) => {
    try {
      await createBook(bookData);
      loadBooks();
      setShowForm(false);
    } catch (error) {
      console.error('Error adding book:', error);
    }
  };

  const handleDeleteBook = async (id) => {
    try {
      await deleteBook(id);
      loadBooks();
    } catch (error) {
      console.error('Error deleting book:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>My Library Tracker</h1>
        <button onClick={() => setShowForm(!showForm)}>
          {showForm ? 'Cancel' : 'Add New Book'}
        </button>
      </header>
      {showForm && <BookForm onSubmit={handleAddBook} />}
      <BookList books={books} onDelete={handleDeleteBook} />
    </div>
  );
}

export default App;
