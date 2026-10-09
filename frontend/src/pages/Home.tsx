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
    <main className="grid min-h-screen place-items-center p-6">
      <section
        className="w-full max-w-[560px] rounded-2xl border border-slate-200 bg-white p-10 shadow-[0_16px_40px_rgb(15_23_42_/_8%)]"
        aria-labelledby="page-title"
      >
        <p className="mb-2.5 text-xs font-bold tracking-[0.08em] text-blue-600 uppercase">
          React + FastAPI starter
        </p>
        <h1
          className="mb-6 text-[clamp(1.8rem,5vw,2.4rem)] font-bold"
          id="page-title"
        >
          Backend connection
        </h1>
        {isLoading && <p role="status">Connecting to the backend…</p>}
        {message && (
          <p className="m-0 rounded-[10px] bg-green-50 px-4 py-3.5 leading-6 text-green-800">
            {message}
          </p>
        )}
        {error && (
          <p
            className="m-0 rounded-[10px] bg-red-50 px-4 py-3.5 leading-6 text-red-800"
            role="alert"
          >
            Could not connect to the backend: {error}
          </p>
        )}
      </section>
    </main>
  );
}
