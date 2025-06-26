import FileUpload from "./components/FileUpload";
import Chat from "./components/Chat";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center bg-gray-900 text-white p-6 sm:p-12 md:p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold text-center mb-8 bg-gradient-to-r from-blue-400 to-purple-500 text-transparent bg-clip-text">
          MyAgent
        </h1>

        <div className="mb-8 p-4 border border-dashed border-gray-600 rounded-lg">
          <FileUpload />
        </div>

        <Chat />
      </div>
    </main>
  );
}
