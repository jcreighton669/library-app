import React, { useState } from 'react';
import { addProgress, updateProgress } from '../api';

function ProgressForm({ bookId, progressId, onSubmit }) {
  const [formData, setFormData] = useState({
    start_date: '',
    current_page: '',
    status: 'to-read',
    target_finish_date: '',
    notes: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (progressId) {
        await updateProgress(progressId, formData);
      } else {
        await addProgress(bookId, formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error updating progress:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="date"
        name="start_date"
        placeholder="Start Date"
        value={formData.start_date}
        onChange={handleChange}
      />
      <input
        type="number"
        name="current_page"
        placeholder="Current Page"
        value={formData.current_page}
        onChange={handleChange}
      />
      <select name="status" value={formData.status} onChange={handleChange}>
        <option value="to-read">To Read</option>
        <option value="reading">Reading</option>
        <option value="paused">Paused</option>
        <option value="finished">Finished</option>
      </select>
      <input
        type="date"
        name="target_finish_date"
        placeholder="Target Finish Date"
        value={formData.target_finish_date}
        onChange={handleChange}
      />
      <textarea
        name="notes"
        placeholder="Notes"
        value={formData.notes}
        onChange={handleChange}
      />
      <button type="submit">{progressId ? 'Update Progress' : 'Start Reading'}</button>
    </form>
  );
}

export default ProgressForm;
