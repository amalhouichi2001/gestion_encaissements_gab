import React, { useEffect, useState } from "react";

function App() {
  const [encaissements, setEncaissements] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/encaissements")
      .then((response) => response.json())
      .then((data) => setEncaissements(data))
      .catch((error) => console.error("Erreur lors du chargement :", error));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-2xl">
        <h1 className="text-2xl font-bold text-gray-800 mb-4 text-center">
          Liste des Encaissements
        </h1>
        <ul className="divide-y divide-gray-300">
          {encaissements.map((encaissement) => (
            <li key={encaissement.id} className="p-4 hover:bg-gray-50">
              <div className="flex justify-between items-center">
                <span className="text-gray-600">
                  {encaissement.date_encaissement}
                </span>
                <span className="font-semibold text-blue-600">
                  {encaissement.montant} TND
                </span>
                <span className="text-gray-500">{encaissement.moyen_paiement}</span>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
