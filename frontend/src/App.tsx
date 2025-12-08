// frontend/src/App.tsx
import { useState, useEffect } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { getItems, createItem } from './services/api';

function App() {
  const [newItem, setNewItem] = useState('');
  const queryClient = useQueryClient();

  // Fetch items
  const { data: items = [], isLoading } = useQuery({
    queryKey: ['items'],
    queryFn: getItems,
  });

  // Add new item
  const { mutate: addItem } = useMutation({
    mutationFn: (name: string) => createItem({ name }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
      setNewItem('');
    },
  });

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Items List</h1>
      
      {/* Add Item Form */}
      <div className="flex gap-2 mb-6">
        <input
          type="text"
          value={newItem}
          onChange={(e) => setNewItem(e.target.value)}
          placeholder="New item name"
          className="flex-1 p-2 border rounded"
        />
        <button
          onClick={() => addItem(newItem)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Add Item
        </button>
      </div>

      {/* Items List */}
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <ul className="space-y-2">
          {items.map((item: any) => (
            <li key={item.id} className="p-3 bg-gray-100 rounded">
              {item.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;