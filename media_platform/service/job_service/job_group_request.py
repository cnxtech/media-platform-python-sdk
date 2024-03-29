from media_platform.http.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.job.job import Job
from media_platform.service.job_service.job_group_response import _JobGroupResponse
from media_platform.service.media_platform_request import MediaPlatformRequest


class JobGroupRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client, base_url):
        # type: (AuthenticatedHTTPClient, str) -> None
        super(JobGroupRequest, self).__init__(authenticated_http_client, 'GET', base_url + '/jobs/', _JobGroupResponse)

        self.group_id = None

        self._url = base_url + '/jobs/groups/'

    def set_group_id(self, group_id):
        # type: (str) -> JobGroupRequest
        self.group_id = group_id
        return self

    def execute(self):
        # type: () -> [Job]

        self.url = self._url + self.group_id

        return super(JobGroupRequest, self).execute().jobs
