namespace rnet.lib
{
    /// <summary>
    /// Interface to communicate with rpy process.
    /// </summary>
    public interface IRPYProcess
    {
        /// <summary>
        /// Start RPY process 
        /// </summary>
        void Start();

        /// <summary>
        /// Create a switch to work like a digital pin, to write two state on/off
        /// </summary>
        /// <param name="pin"></param>
        /// <returns>ISwitch object</returns>
        ISwitch Switch { get; }

        /// <summary>
        /// To write PWM values in a pin, accepted values from 0 to 100
        /// </summary>
        /// <param name="pin"></param>
        /// <returns></returns>
        IPWM PWM { get; }

        /// <summary>
        /// Call exit to cleanup all rpy process
        /// </summary>
        void Exit();
    }
}
