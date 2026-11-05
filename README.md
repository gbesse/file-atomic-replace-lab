# file-atomic-replace-lab

## Français

Tuer un écrivain avant et après remplacement atomique de fichier.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m file_atomic_replace_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Un vrai enfant écrit et fsync le temporaire ; SIGKILL avant/après os.replace vérifie contenu et résidu. L’exemple ne se contente pas de simuler un statut de crash.

### Limites

POSIX local, même répertoire ; ne teste ni panne électrique ni durabilité du répertoire après perte d’alimentation.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Kill a writer before and after atomic file replacement.

Synthetic data; no network access or secret required.

```sh
python -m file_atomic_replace_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

An actual child writes and fsyncs a temporary file; SIGKILL before/after os.replace checks content and residue. Does not merely simulate crash status.

### Limits

Local POSIX, same directory; does not test power failure or directory durability after power loss.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Matar un escritor antes y después de reemplazo atómico de archivo.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m file_atomic_replace_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Un hijo real escribe y sincroniza temporal; SIGKILL antes/después de os.replace comprueba contenido y residuo. No solo simula estado de fallo.

### Límites

POSIX local, mismo directorio; no prueba corte eléctrico ni durabilidad de directorio tras pérdida de alimentación.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.python.org/3/library/os.html#os.replace
