import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [pantallaActual, setPantallaActual] = useState<'menu' | 'maquina' | 'salida'>('menu');
  const [pantallaVisible, setPantallaVisible] = useState(true);
  const [pendingPantalla, setPendingPantalla] = useState<'menu' | 'maquina' | 'salida' | null>(null);
  const [selectedOption, setSelectedOption] = useState('');
  const [isAnimating, setIsAnimating] = useState(false);

  const handleCafeSelect = (option: string) => {
    setSelectedOption(option);
    setIsAnimating(false);
    setTimeout(() => setIsAnimating(true), 10);
  };

  const cambiarPantalla = (nuevaPantalla: 'menu' | 'maquina' | 'salida') => {
    setPantallaVisible(false);
    setPendingPantalla(nuevaPantalla);
  };

  useEffect(() => {
    if (!pantallaVisible && pendingPantalla) {
      const timer = setTimeout(() => {
        setPantallaActual(pendingPantalla);
        setPantallaVisible(true);
        setPendingPantalla(null);
        setSelectedOption('');
        setIsAnimating(false);
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [pantallaVisible, pendingPantalla]);

  useEffect(() => {
    if (selectedOption) {
      const timer = setTimeout(() => {
        setSelectedOption('');
        setIsAnimating(false);
      }, 5000);
      return () => clearTimeout(timer);
    }
  }, [selectedOption]);

  return (
    <div className={`pantalla ${pantallaVisible ? 'fade-in' : 'fade-out'}`}>
      {pantallaActual === 'menu' && (
        <div className="machine-container">
          <h1 className="title">☕ Bienvenido a Café Leblanc</h1>
          <p>¿Qué deseas hacer?</p>
          <div className="buttons">
            <button onClick={() => cambiarPantalla('maquina')}>Entrar a la máquina de café</button>
            <button className="boton-salir" onClick={() => cambiarPantalla('salida')}>
              Salir
            </button>
          </div>
        </div>
      )}

      {pantallaActual === 'salida' && (
        <div className="machine-container">
          <h1 className="title">Gracias por visitarnos ☕</h1>
          <p>¡Vuelve pronto!</p>
        </div>
      )}

      {pantallaActual === 'maquina' && (
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
            {selectedOption ? `Has seleccionado: ${selectedOption}` : 'Selecciona una opción'}
          </div>

          <div className="coffee-animation-container">
            <div className={`coffee-animation ${isAnimating ? 'active' : ''}`} />
          </div>

          <div className="coffee-cup">☕</div>

          <button onClick={() => cambiarPantalla('menu')} style={{ marginTop: '20px' }}>
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
      )}
    </div>
  );
}

export default App;
