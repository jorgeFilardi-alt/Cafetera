import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [pantallaActual, setPantallaActual] = useState<'menu' | 'maquina' | 'salida'>('menu');
  const [selectedOption, setSelectedOption] = useState('');
  const [isAnimating, setIsAnimating] = useState(false);

  const handleCafeSelect = (option: string) => {
    setSelectedOption(option);
    setIsAnimating(false);
    setTimeout(() => setIsAnimating(true), 10);
  };

  useEffect(() => {
    if (selectedOption) {
      const timer = setTimeout(() => {
        setSelectedOption('');
        setIsAnimating(false);
      }, 5000);
      return () => clearTimeout(timer);
    }
  }, [selectedOption]);

  if (pantallaActual === 'menu') {
    return (
      <div className="machine-container">
        <h1 className="title">☕ Bienvenido a Café Leblanc</h1>
        <p>¿Qué deseas hacer?</p>
        <div className="buttons">
          <button onClick={() => setPantallaActual('maquina')}>Entrar a la máquina de café</button>
          <button className="boton-salir" onClick={() => setPantallaActual('salida')}>
            Salir
          </button>
        </div>
      </div>
    );
  }

  if (pantallaActual === 'salida') {
    return (
      <div className="machine-container">
        <h1 className="title">Gracias por visitarnos ☕</h1>
        <p>¡Vuelve pronto!</p>
      </div>
    );
  }

  // Pantalla de la máquina de café
  return (
    <div className="machine-container">
      <h1 className="title">☕ Dispensador de Café</h1>

      <div className="buttons">
        <button onClick={() => handleCafeSelect('Café Solo')}>Café Solo</button>
        <button onClick={() => handleCafeSelect('Café con Leche')}>Café con Leche</button>
        <button onClick={() => handleCafeSelect('Café con birra')}>Café con birra</button>
        <button onClick={() => handleCafeSelect('Capuccino')}>Capuccino</button>
        <button onClick={() => handleCafeSelect('Café Irlandés')}>Café Irlandés</button>
        <button onClick={() => handleCafeSelect('Latte')}>Latte</button>
      </div>

      <div className="display">
        {selectedOption
          ? `Has seleccionado: ${selectedOption}`
          : 'Selecciona una opción'}
      </div>

      <div className="coffee-animation-container">
        <div className={`coffee-animation ${isAnimating ? 'active' : ''}`} />
      </div>

      <div className="coffee-cup">☕</div>

      <button onClick={() => setPantallaActual('menu')} style={{ marginTop: '20px' }}>
        Volver al menú principal
      </button>

      <footer className="footer">
        <p>© 2025 Café Leblanc</p>
        <div className="footer-links">
          <a href="#">Contacto</a>
          <a href="#">Servicios</a>
          <a href="mailto:cafeleblanc@ejemplo.com">Correo</a>
          <a href="#">Ubicación</a>
      </div>
      </footer>
    </div>
  );
}

export default App;
