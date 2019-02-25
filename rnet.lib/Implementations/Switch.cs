using System;
using System.Collections.Generic;

namespace rnet.lib.Implementations
{
    public class Switch : ISwitch
    {

        private readonly RPYProcess rpyProcess;
        private readonly int pin;

        public Switch(RPYProcess rpyProcess)
        {
            this.rpyProcess = rpyProcess;
        }

        public Switch(RPYProcess rpyProcess, int pin)
        {
            this.rpyProcess = rpyProcess;
            this.pin = pin;
        }

        private IDictionary<int, ISwitch> Switchs { get; } = new Dictionary<int, ISwitch>();

        public ISwitch this[int pin]
        {
            get
            {
                if (!Switchs.ContainsKey(pin))
                {
                    Switchs[pin] = new Switch(rpyProcess, pin);
                }
                return Switchs[pin];
            }
        }

        public void Write(bool value)
        {
            lock (rpyProcess.@lock)
            {
                Console.WriteLine($"Write {value}");
                rpyProcess.BeginStandardInputWrite();

                rpyProcess.standardInput.WriteLine($"led pin={pin} value={(value == true ? 1 : 0)}");///Executing command

                Console.WriteLine($"Waiting {value}");
                rpyProcess.EndStandardInputWrite();
                Console.WriteLine($"Stop Waiting {value}");
            }
        }

    }
}
