from weatheradvicer.cli import get_temp, url_formatted
from unittest.mock import patch, Mock


@patch("requests.get")
def test_get_temp(mocked_request):
    mocked_request.return_value = Mock(
        status_code=200,
        json=Mock(return_value={"cod": 200, "main": {"temp": 287.74}}),
    )
    temp = get_temp()
    assert type(temp) == int
    assert temp == 15
    mocked_request.assert_called_with(url_formatted)
