Bezüglich der Aufgabe.

Ich habe ungefähr 10 Stunden plus eine Vorbereitung benötigt. Bezüglich der Laufzeit lässt sich feststellen, 
dass nahezu alle Operationen in linearer Zeit ablaufen, 
abgesehen von dem Aufruf .sort() (zeile 205 in der main() Methode). 
Dieser unterläuft eine Laufzeit mit einer oberen Schranke von O(n*log(n)). 
Wie geschildert gibt es weitere Operationen die in O(1) ablaufen wie 
das Einlesen, das Konvertieren, oder das Mergen selbst.

Bezüglich der Robustheit habe ich ein Exceptionhandling eingebaut, welches, 
zu mindest meiner bisherigen Erkenntnis nach, alle Fehleingaben abfangen sollte. 

Es handelt sich um einen Konsolen aufruf mit Tastatur Eingaben geschrieben in python.
Natürlich hätte ich die Intervalle auch Direkt einlesen können, anstatt als String, 
ich wollte jedoch eine Textfeld Eingabe, wie zum Beispiel in einem Frontend, simulieren.
Darüber hinaus, vereinfachte dies, die Produktion von robustem Code bzw. den Hinweis auf solchen.

Zunächst wird bei der Eingabe nach der Anzahl der Intervalle gefragt, diese ist aktuell auf maximal 8 beschränkt. 
Dies kann jedoch bei Bedarf angepasst werden. Danach werden die einzelnen Intervalle im wie folgend angegeben: [1, 2]
Falls mit Robustheit bei großen Eingaben, eine Eingabe von sehr vielen Intervallen in kurzen Zeit gemeint gewesen sein sollte, 
so müsste ein Queing System(z.b. MessageQueue) vorgeschaltet werden und die Zwischenergebnisse in z.b. einem Buffer zwischen gespeichert werden.

Falls nach einer Laufzeitanalyse im Code selbst mit einer Ausgabe am Ende gefragt gewesen sein sollte, kann diese gerne auf Bedarf nach gereicht werden.
Dies sollte in python nur wenig weiteren Aufwand verursachen.

Eine Speicheranalyse befindet sich im root Verzeichniss und trägt den Namen "memory.txt". Sie wurde mit 8 Intervallen ausgeführt mit Zahlen von 1 bis 258. Sie hat laut Profiler 20.7111 mb beansprucht.
Dies lässt sich sicher noch optimieren.

Die Applikation liegt im Ordner "dist/mergeIntervals" und trägt den Namen mergeIntervals.exe. 
Falls ebenfalls nach einer Ausführbarkeit via Script in Linux gefragt gewesen sein sollte, ließe sich dies ebenfalls nachreichen.
