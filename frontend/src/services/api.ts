// frontend/src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/items', // Your FastAPI server
});

// Items API
export const getItems = async () => {
  const response = await api.get('/');
  return response.data;
};

export const createItem = async (itemData: any) => {
  const response = await api.post('/', itemData);
  return response.data;
};

// Add more API calls as needed