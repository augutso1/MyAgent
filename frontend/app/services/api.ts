// Upload frontend
export async function uploadDocument(file: File) {

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://localhost:8000/api/v1/upload", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {

            const errorData = await response.json();
            throw new Error(errorData.detail || "Falha ao fazer upload do arquivo.");
        }

        return await response.json();
    } catch (error) {
        console.error("Erro na chamada de API para upload:", error);
        throw error;
    }
}

// Chat frontend
export async function sendQuery(question: string) {
    try {
        const response = await fetch("http://localhost:8000/api/v1/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ question: question }), // Enviamos a pergunta como um JSON
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Falha ao enviar a pergunta.");
        }

        return await response.json();
    } catch (error) {
        console.error("Erro na chamada de API para query:", error);
        throw error;
    }
}