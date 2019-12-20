using System;
using System.Collections.Generic;

namespace rnet.lib.Implementations.Live
{
    public class LiveSwitch : ISwitch
    {

        private readonly LiveProcess rpyProcess;
        private readonly int pin;

        public LiveSwitch(LiveProcess rpyProcess)
        {
            this.rpyProcess = rpyProcess;
        }

        public LiveSwitch(LiveProcess rpyProcess, int pin)
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
                    Switchs[pin] = new LiveSwitch(rpyProcess, pin);
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
