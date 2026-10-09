import { useEffect, useState } from "react";
import axios from "axios";
import api from "../api/api";
import type { TestResponse } from "../api/types";

export default function Home() {
  const [message, setMessage] = useState<string>("");
  const [error, setError] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    let isMounted = true;

    async function checkBackend(): Promise<void> {
      try {
        const response = await api.get<TestResponse>("/api/test");
        if (isMounted) {
          setMessage(response.data.message);
        }
      } catch (requestError: unknown) {
        if (isMounted) {
          setError(
            axios.isAxiosError(requestError)
              ? requestError.message
              : "An unexpected error occurred while connecting to the backend.",
          );
        }
      } finally {
        if (isMounted) {
          setIsLoading(false);
        }
      }
    }

    void checkBackend();
    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <main className="home">
      <section className="status-card" aria-labelledby="page-title">
        <p className="eyebrow">React + FastAPI starter</p>
        <h1 id="page-title">Backend connection</h1>
        {isLoading && <p role="status">Connecting to the backend…</p>}
        {message && <p className="success-message">{message}</p>}
        {error && (
          <p className="error-message" role="alert">
            Could not connect to the backend: {error}
          </p>
        )}
      </section>
    </main>
  );
}
