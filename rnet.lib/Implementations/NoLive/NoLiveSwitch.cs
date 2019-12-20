using System;
using System.Collections.Generic;

namespace rnet.lib.Implementations.NoLive
{
    public class NoLiveSwitch : ISwitch
    {

        private readonly NoLiveProcess rpyProcess;
        private readonly int pin;

        public NoLiveSwitch(NoLiveProcess rpyProcess)
        {
            this.rpyProcess = rpyProcess;
        }

        public NoLiveSwitch(NoLiveProcess rpyProcess, int pin)
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
                    Switchs[pin] = new NoLiveSwitch(rpyProcess, pin);
                }
                return Switchs[pin];
            }
        }

        public void Write(bool value)
        {
            lock (rpyProcess.@lock)
            {
                Console.WriteLine($"Write {value}");

                var sql = $"led pin={pin} value={(value == true ? 1 : 0)}";///Executing command
                rpyProcess.ExcecuteCommand(sql);

                Console.WriteLine($"Stop Waiting {value}");
            }
        }

    }
}
