class Motor(object):
  def __init__(self, name, binary, energy_cost, energy_spent):
    self._name = name
    self._binary = binary
    self._energy_cost = energy_cost
    self._energy_spent = energy_spent

  def get_name(self):
    return self._name

  def get_binary(self):
    return self._binary

  def get_energy_cost(self):
    return self._energy_cost

  def get_energy_spent(self):
    return self._energy_spent

  def __repr__(self):
    return '        <Motor>\n' + \
           '          <name>' + str(self._name.decode('utf-8')) + \
           '</name>\n' + \
           '          <binary>' + str(self._binary) + '</binary>\n' + \
           '          <energy_cost>' + \
           str(self._energy_cost) + '</energy_cost>\n' + \
           '        </Motor>\n'

  def __str__(self):
    return self.__repr__()

  def __unicode__(self):
    return self.__repr__()
