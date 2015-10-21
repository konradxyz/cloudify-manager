from windows_agent_installer.winrm_runner import WinRMRunner

agent = {
  'host': '15.126.224.128',
  'user': 'Administrator',
  'password': '@dm1n',
  'transport': 'plaintext'
}

agent = {
  'host': '15.126.224.128',
  'user': 'kp/user',
  'password': 'dom@1nDOMAIN',
  'transport': 'kerberos'
}

runner = WinRMRunner(agent, validate_connection=False)

runner.test_connectivity()

