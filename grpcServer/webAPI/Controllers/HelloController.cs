using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using webAPI.Models;

namespace webAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class HelloController : ControllerBase
    {
        private readonly ILogger<HelloController> _logger;

        public HelloController(ILogger<HelloController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public string SayHello(string name)
        {
            return "Hello " + name;
        }

        [HttpPost]
        public SayHelloResponse SayHello2(SayHelloRequest sayHelloRequest)
        {
            var sayHelloResponse = new SayHelloResponse();
            sayHelloResponse.Message = "Hello " + sayHelloRequest.Name;

            return sayHelloResponse;
        }
    }
}
