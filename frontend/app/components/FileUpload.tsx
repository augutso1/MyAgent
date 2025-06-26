"use client";

import { useState, useRef } from "react";
import { uploadDocument } from "../services/api";

export default function FileUpload() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const [uploadStatus, setUploadStatus] = useState<
    "idle" | "uploading" | "success" | "error"
  >("idle");

  const [message, setMessage] = useState("");

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      setUploadStatus("idle");
      setMessage(`Arquivo selecionado: ${file.name}`);
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setMessage("Por favor, selecione um arquivo primeiro.");
      return;
    }

    setUploadStatus("uploading");
    setMessage("Enviando arquivo...");

    try {
      const response = await uploadDocument(selectedFile);
      setUploadStatus("success");
      setMessage(response.message);
    } catch (error) {
      setUploadStatus("error");
      if (error instanceof Error) {
        setMessage(`Erro: ${error.message}`);
      } else {
        setMessage("Ocorreu um erro desconhecido.");
      }
    }
  };

  const handleButtonClick = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="w-full">
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        style={{ display: "none" }}
        accept=".pdf"
      />

      <button
        onClick={handleButtonClick}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-2"
      >
        Selecionar Arquivo PDF
      </button>

      {selectedFile && (
        <button
          onClick={handleUpload}
          disabled={uploadStatus === "uploading"}
          className="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded disabled:bg-gray-500"
        >
          {uploadStatus === "uploading"
            ? "Enviando..."
            : "Fazer Upload e Indexar"}
        </button>
      )}

      {message && (
        <p
          className={`mt-4 text-center ${
            uploadStatus === "error" ? "text-red-400" : "text-gray-300"
          }`}
        >
          {message}
        </p>
      )}
    </div>
  );
}
