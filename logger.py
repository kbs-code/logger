from datetime import datetime

class LoggerBase:
  def __init__(self, output):
    self.output = output

  def _log(self, level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {level.upper()}: {message}"
    self.output(log_entry)

  def info(self, message):
    self._log("INFO", message)

  def warn(self, message):
    self._log("WARNING", message)

  def error(self, message):
    self._log("ERROR", message)

class StdoutLogger(LoggerBase):
  def __init__(self):
    super().__init__(print)

class FileLogger(LoggerBase):
  def __init__(self, filename="events.log"):
    self.filename = filename
    super().__init__(self._write_to_file)

  def _write_to_file(self, log_entry):
    with open(self.filename, "a") as f:
      f.write(log_entry + "\n")

class Logger:
  def __init__(self):
    self.out = StdoutLogger()
    self.file = FileLogger()

log = Logger()