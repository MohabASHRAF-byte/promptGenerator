// src/components/hooks/useDebounce.js
import { useState, useEffect } from "react";

// value: any value to debounce
// delay: ms to wait after last change
export default function useDebounce(value, delay) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const handler = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(handler);
  }, [value, delay]);
  return debounced;
}
