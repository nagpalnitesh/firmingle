var app = angular.module("firmodule", []);

app.controller("fircontroller", function ($scope, $window, $http, $timeout) {
  $scope.creating_user = function (x = true) {
    if (
      $scope.signup_firstname == undefined ||
      $scope.signup_lastname == undefined ||
      $scope.signup_email == undefined ||
      $scope.signup_password == undefined ||
      $scope.signup_cfpassword == undefined
    ) {
      alert("Please Fill The Details Properly");
      return;
    }
    if (!x) {
      return;
    }
    $http({
      method: "POST",
      url: "/invited_user/",
      data: {
        firstname: $scope.signup_firstname,
        lastname: $scope.signup_lastname,
        password: $scope.signup_password,
        email: $scope.signup_email,
      },
    }).then(
      function (success) {
        $scope.success = success.data.message;
        $scope.succ = true;
        $scope.success = "Saved";
        $scope.signup_firstname = "";
        $scope.signup_lastname = "";
        $scope.signup_email = "";
        $scope.signup_password = "";
        $timeout(function () {
          $scope.succ = false;
        }, 10000);
        alert("Check your mail to activate !!");
      },
      function (error) {
        $scope.showerror = true;
        $scope.err = true;
        $timeout(function () {
          $scope.showerror = false;
        }, 10000);
        $scope.error = error.data["message"];
        alert(error.data["message"]);
      }
    );
  };
  $scope.login_function = function () {
    if ($scope.username == undefined || $scope.password == undefined) {
      alert("Please Fill The Details");
      return;
    }
    $http({
      method: "POST",
      url: "/login/",
      data: { username: $scope.username, password: $scope.password },
    }).then(
      function (success) {
        console.log(success.data);
        $scope.success = success.data.message;
        $scope.succ = true;
        $scope.username = "";
        $scope.password = "";
        $timeout(function () {
          $scope.succ = false;
        }, 10000);
        window.location = "/";
      },
      function (error) {
        $scope.showerror = true;
        console.log(error.data);
        $scope.err = true;
        $timeout(function () {
          $scope.showerror = false;
        }, 10000);
        $scope.error = error.data["message"];
        alert(error.data["message"]);
      }
    );
  };
});
