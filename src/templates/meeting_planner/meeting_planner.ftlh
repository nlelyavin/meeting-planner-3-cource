<#ftl encoding='utf-8'>
<#import '/spring.ftl' as spring>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Teams</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        body {
            background-color: #c7cbcc;
        }

        header {
            width: 200px;
            background-color: #1893ea;
            padding: 10px;
            text-align: left;
            font-size: 10px;
            color: white;
        }

        header2 {
            width: 200px;
            height: 500px;
            background-color: #1893ea;
            padding-left: 400px;
            text-align: left;
            font-size: 10px;
            color: white;
        }

        p {

        }
        .btn1 {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 10px 17px;
            cursor: pointer;
            border-radius: 20px;

        }
        .btn:hover {
            background-color: RoyalBlue;
        }

    </style>
</head>
    <body>
    <nav class="navbar navbar-expand-lg navbar-light " style="background-color: #1893ea" >
        <a class="navbar-brand" style="color: #ffff">Meeting Planner</a>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="<@spring.url '/signIn' />" style="color: #ffff">Войти<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="<@spring.url '/signUp' />" style="color: #ffff">Регистрация</a>
                </li>
            </ul>
        </div>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        </div>
    </nav>

    <div class="container-fluid" >
        <table class="table table-condensed" style="background-color: white; margin-top: 20px;" >
            <thead>
            <tr>

                <td class="col-md-4" style="text-align: center; font-size: x-large" >
                    <div class="text-center">
                        <img src="/img/avarat.jpg" class="rounded" alt=" ">
                    </div>
                    <b style="color: #1893ea">Meeting planner</b> <b> - </b>
                    <br>
                    <b> лучшие решение для планирования внутри вашей команды</b>
                </td>


            </tr>
            </thead>
        </table>
    </div>

    </body>
</html>