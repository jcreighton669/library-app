import React from 'react';

function BookList({ books, onDelete }) {
  return (
    <div className="book-list">
      {books.map(book => (
        <div key={book.id} className="book-card">
          <h3>{book.title}</h3>
          <p><strong>Author:</strong> {book.author}</p>
          {book.isbn && <p><strong>ISBN:</strong> {book.isbn}</p>}
          {book.genres && <p><strong>Genres:</strong> {book.genres}</p>}
          {book.page_count && <p><strong>Pages:</strong> {book.page_count}</p>}
          <button onClick={() => onDelete(book.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}

export default BookList;
