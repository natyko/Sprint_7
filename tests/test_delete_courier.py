import allure


@allure.epic("Courier Management")
@allure.feature("Courier Deletion")
class TestCourierDeletion:

    @allure.title("Test successful courier deletion")
    @allure.description("Check that a courier can be successfully deleted")
    def test_courier_deletion_success(self, courier_helper, registered_courier):
        # Delete an existing courier and verify deletion
        courier_id = registered_courier["id"]
        response = courier_helper.delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}
        # Verify the courier cannot log in after deletion
        login_response = courier_helper.login_courier(
            {
                "login": registered_courier["login"],
                "password": registered_courier["password"],
            }
        )
        assert login_response.status_code == 404

    @allure.title("Test deletion of nonexistent courier ID")
    @allure.description("Verify deleting a nonexistent courier returns a 404 error")
    def test_courier_deletion_nonexistent_id(self, courier_helper):
        response = courier_helper.delete_courier(999999999)
        assert response.status_code == 404
        assert "message" in response.json()
        assert response.json()["message"] != ""
