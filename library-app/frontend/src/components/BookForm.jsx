import React, { useState } from 'react';

function BookForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    title: '',
    author: '',
    isbn: '',
    publisher: '',
    year: '',
    genres: '',
    page_count: '',
    format: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    setFormData({
      title: '',
      author: '',
      isbn: '',
      publisher: '',
      year: '',
      genres: '',
      page_count: '',
      format: ''
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        placeholder="Title"
        value={formData.title}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="author"
        placeholder="Author"
        value={formData.author}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="isbn"
        placeholder="ISBN"
        value={formData.isbn}
        onChange={handleChange}
      />
      <input
        type="text"
        name="publisher"
        placeholder="Publisher"
        value={formData.publisher}
        onChange={handleChange}
      />
      <input
        type="number"
        name="year"
        placeholder="Year"
        value={formData.year}
        onChange={handleChange}
      />
      <input
        type="text"
        name="genres"
        placeholder="Genres (comma separated)"
        value={formData.genres}
        onChange={handleChange}
      />
      <input
        type="number"
        name="page_count"
        placeholder="Page Count"
        value={formData.page_count}
        onChange={handleChange}
      />
      <select name="format" value={formData.format} onChange={handleChange}>
        <option value="">Select Format</option>
        <option value="paperback">Paperback</option>
        <option value="hardcover">Hardcover</option>
        <option value="ebook">E-book</option>
        <option value="audiobook">Audiobook</option>
      </select>
      <button type="submit">Add Book</button>
    </form>
  );
}

export default BookForm;
