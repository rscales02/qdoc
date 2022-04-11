import { FC } from "react";
import {RegisterForm} from '../components/RegisterForm'
interface IRegisterProps {};

export const Register: FC<IRegisterProps> = (props) => {
    return (
        <div>
          <RegisterForm/>
        </div>
    );
}
