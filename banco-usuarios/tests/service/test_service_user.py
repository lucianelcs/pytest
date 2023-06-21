from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        name_add = 'Luciane Santos'
        job_add = 'TechLead'
        wait_result = 'User added successfully'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert wait_result == result

    def test_existing_user(self):
        name_rep = 'Luciane'
        job_rep = 'TechLead'
        wait_result = 'User already exists'
        service = ServiceUser()

        result = service.add_user(name=name_rep, job=job_rep)

        assert wait_result == result

    def test_null_user(self):
        name_null = None
        job_null = 'Tester'
        wait_result = 'Invalid User'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert wait_result == result

    def test_validate_null_job(self):
        name_null = 'Luciane'
        job_null = None
        wait_result = 'Invalid User'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert wait_result == result

    def test_validate_invalid_user(self):
        name_inv = 20
        job_inv = 'Tester'
        wait_result = 'Name or job need to be string'
        service = ServiceUser()

        result = service.add_user(name=name_inv, job=job_inv)

        assert wait_result == result

    def test_invalid_job(self):
        name_inv = 'Luciane'
        job_inv = 100
        wait_result = 'Name or job need to be string'
        service = ServiceUser()

        result = service.add_user(name=name_inv, job=job_inv)

        assert wait_result == result

    def test_select_user_success(self):
        name = 'Luciane'
        wait_result = 'Job: QA Engineer'
        service = ServiceUser()

        result = service.select_user(name=name)

        assert wait_result == result

    def test_update_job_success(self):
        name = 'Luciane'
        job = 'Tech Lead'
        wait_result = 'Job was updated'
        service = ServiceUser()

        result = service.update_user(name=name, new_job=job)

        assert wait_result == result

    def test_update_job_invalid_user(self):
        name = 'joão '
        job = 'TechLead'
        wait_result = 'User name is not found'
        service = ServiceUser()

        result = service.update_user(name=name, new_job=job)

        assert wait_result == result

    def test_update_job_with_null_user(self):
        name = None
        job = 'TechLead'
        wait_result = 'User name is not found'
        service = ServiceUser()

        result = service.update_user(name=name, new_job=job)

        assert wait_result == result

    def test_select_invalid_user(self):
        name = 'João'
        wait_result = 'User name is not found'
        service = ServiceUser()

        result = service.select_user(name=name)

        assert wait_result == result

    def test_select_null_user(self):
        name = None
        wait_result = 'User name is not found'
        service = ServiceUser()

        result = service.select_user(name=name)

        assert wait_result == result

    def test_delete_user_success(self):
        name = 'Luciane'
        wait_result = 'User was removed'
        service = ServiceUser()

        result = service.delete_user(name=name)

        assert wait_result == result

    def test_delete_invalid_user(self):
        name = 'João '
        wait_result = 'User name is not found'
        service = ServiceUser()

        result = service.delete_user(name=name)

        assert wait_result == result

    def test_delete_null_user(self):
        name = None
        wait_result = 'User name is not found'
        service = ServiceUser()

        result = service.delete_user(name=name)

        assert wait_result == result
